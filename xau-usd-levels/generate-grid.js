const fs = require('fs');

function extendTemplate() {
    const tplContent = fs.readFileSync('XAU-Black-mt5.tpl', 'utf16le');
    
    // 1. Extract all existing POI prices
    const priceRegex = /<object>[\s\S]*?type=1[\s\S]*?value1=([\d\.]+)[\s\S]*?<\/object>/g;
    let match;
    const prices = [];
    
    while ((match = priceRegex.exec(tplContent)) !== null) {
        prices.push(parseFloat(match[1]));
    }
    
    if (prices.length === 0) {
        console.error("No existing horizontal lines found.");
        return;
    }
    
    const maxPrice = Math.max(...prices);
    const minPrice = Math.min(...prices);
    
    // 2. Grid Configuration
    const POI_STEP = 11.5;
    const SUB_POI_STEP = 5.75; // Exactly halfway
    
    // Adjust these to add more levels above/below your current grid
    const LEVELS_TO_EXTEND_UP = 20;   
    const LEVELS_TO_EXTEND_DOWN = 20; 
    
    // MT5 Colors (BGR Integer Format)
    const MAIN_COLOR = 65535;      // Existing Yellow
    const SUB_COLOR = 12632256;    // Silver/Gray (Change as needed)
    
    let newObjects = "";
    let addedCount = 0;
    
    const createLine = (price, color, style, width) => {
        addedCount++;
        // style: 0 = Solid, 1 = Dashed
        return `
<object>
type=1
name=${price.toFixed(2)}
color=${color}
style=${style}
width=${width}
value1=${price.toFixed(6)}
</object>`;
    };

    // Calculate total generation range
    const lowestTarget = minPrice - (LEVELS_TO_EXTEND_DOWN * POI_STEP);
    const highestTarget = maxPrice + (LEVELS_TO_EXTEND_UP * POI_STEP);
    
    // Align starting point strictly to the mathematical grid
    let currentPrice = minPrice;
    while (currentPrice > lowestTarget) {
        currentPrice -= POI_STEP;
    }
    
    // 3. Generate the ladder (Backfilling Sub-POIs and creating new Main POIs)
    while (currentPrice <= highestTarget) {
        // Floating point safe check to see if main POI already exists
        const isExisting = prices.some(p => Math.abs(p - currentPrice) < 0.01);
        
        if (!isExisting) {
            // New Main POI (Dashed)
            newObjects += createLine(currentPrice, MAIN_COLOR, 1, 1);
        }
        
        // Sub-POI (Solid, Width 1, Midpoint)
        const subPrice = currentPrice + SUB_POI_STEP;
        if (subPrice <= highestTarget) {
            newObjects += createLine(subPrice, SUB_COLOR, 0, 1);
        }
        
        currentPrice += POI_STEP;
    }
    
    // 4. Update total object count so MT5 doesn't truncate the file
    let updatedTpl = tplContent;
    const objectsCountRegex = /objects=(\d+)/;
    const countMatch = updatedTpl.match(objectsCountRegex);
    
    if (countMatch) {
        const currentCount = parseInt(countMatch[1], 10);
        updatedTpl = updatedTpl.replace(`objects=${currentCount}`, `objects=${currentCount + addedCount}`);
    }
    
    // 5. Inject the new objects safely at the end of the file
    const lastObjectPos = updatedTpl.lastIndexOf("</object>");
    if (lastObjectPos !== -1) {
        const before = updatedTpl.substring(0, lastObjectPos + 9);
        const after = updatedTpl.substring(lastObjectPos + 9);
        updatedTpl = before + "\n" + newObjects + after;
    }
    
    fs.writeFileSync('XAU-Black-mt5-extended.tpl', updatedTpl, 'utf16le');
    console.log(`Grid extended! Added ${addedCount} new lines. Saved to XAU-Black-mt5-extended.tpl`);
}

extendTemplate();