async function extractAndDownloadAllTradeGrids() {
    console.log("Initializing Omni-Date SPA Extractor...");

    // 1. Aggressive Date Extraction
    let formattedDate = "UnknownDate";
    let rawDateStr = null;
    
    // Catch: "August 1, 2024", "Aug 1 2024", "08/01/2024", "2024-08-01"
    const dateRegexes = [
        /(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}(?:st|nd|rd|th)?(?:,)?\s+\d{4}/i,
        /\d{1,2}\/\d{1,2}\/\d{4}/,
        /\d{4}-\d{2}-\d{2}/
    ];

    const allText = document.body.innerText;

    // Scan static text first
    for (let rx of dateRegexes) {
        const match = allText.match(rx);
        if (match) {
            rawDateStr = match[0];
            break;
        }
    }

    // Fallback: Scan editable input fields (SPA titles are often inputs)
    if (!rawDateStr) {
        const inputs = Array.from(document.querySelectorAll('input[type="text"]'));
        for (let input of inputs) {
            for (let rx of dateRegexes) {
                const match = input.value.match(rx);
                if (match) {
                    rawDateStr = match[0];
                    break;
                }
            }
            if (rawDateStr) break;
        }
    }

    // Parse and Format
    if (rawDateStr) {
        const d = new Date(rawDateStr);
        if (!isNaN(d.getTime())) { // Ensure it's a valid date object
            const yyyy = d.getFullYear();
            const mm = String(d.getMonth() + 1).padStart(2, '0');
            const dd = String(d.getDate()).padStart(2, '0');
            formattedDate = `${yyyy}-${mm}-${dd}`;
            console.log(`📅 Found active date: "${rawDateStr}" -> Converted to: ${formattedDate}`);
        } else {
            console.warn(`⚠️ Found "${rawDateStr}" but failed to parse it into a real date.`);
        }
    } else {
        console.warn("⚠️ Could not locate any valid date string on screen. Defaulting to 'UnknownDate'.");
    }

    // 2. SPA Fix: Find ALL VISIBLE tables
    const allWrappers = document.querySelectorAll('.PlaygroundEditorTheme__tableScrollableWrapper');
    let activeTables = [];
    
    for (const wrapper of allWrappers) {
        if (wrapper.getBoundingClientRect().height > 0) {
            activeTables.push(wrapper);
        }
    }

    if (activeTables.length === 0) {
        console.error("❌ No visible tables found in the active view.");
        return;
    }

    console.log(`✅ Found ${activeTables.length} active table(s) to process.`);

    // 3. Process each table sequentially
    for (let t = 0; t < activeTables.length; t++) {
        const table = activeTables[t];
        console.log(`\n⚙️ Processing Table ${t + 1} of ${activeTables.length}...`);
        
        const rows = table.querySelectorAll('tr, .PlaygroundEditorTheme__tableRow');
        if (rows.length === 0) {
            console.warn(`⚠️ No rows found in Table ${t + 1}. Skipping.`);
            continue;
        }

        // 4. Extract Headers
        const headerCells = rows[0].querySelectorAll('th, td, .PlaygroundEditorTheme__tableCell');
        const headers = Array.from(headerCells).map((cell, index) => {
            let text = cell.innerText.trim().replace(/[^a-zA-Z0-9]/g, '_');
            return text ? text : `Col${index}`;
        });
        
        console.log(`   Mapped Timeframes: [${headers.join(', ')}]`);

        // 5. Iterate Rows and Download
        for (let r = 1; r < rows.length; r++) {
            const cells = rows[r].querySelectorAll('td, .PlaygroundEditorTheme__tableCell');
            
            for (let c = 0; c < cells.length; c++) {
                const img = cells[c].querySelector('img');
                
                if (img && img.src) {
                    const timeframe = headers[c];
                    
                    // Filename formatting
                    const filename = `${formattedDate}_T${t + 1}_Trade_${r}_${timeframe}.png`;
                    console.log(`   ⬇️ Fetching: ${filename}...`);

                    try {
                        const response = await fetch(img.src);
                        const blob = await response.blob();

                        const url = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.style.display = 'none';
                        a.href = url;
                        a.download = filename;
                        
                        document.body.appendChild(a);
                        a.click();
                        
                        window.URL.revokeObjectURL(url);
                        a.remove();
                        
                        await new Promise(resolve => setTimeout(resolve, 500)); 
                        
                    } catch (err) {
                        console.error(`   ❌ Failed to download ${filename}:`, err);
                    }
                }
            }
        }
    }
    console.log("\n✅ All images downloaded and mapped to standard dates successfully.");
}

extractAndDownloadAllTradeGrids();