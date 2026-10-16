const preProcess = (t) => {
    return t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        .replace(/\s*[-\u2010\u2011\u2013\u2014\u2212]+\s*/g, ' - ');
};

const clean = (w) => w.toLowerCase().trim();

function diffWords(userText, targetText) {
    const uWords = preProcess(userText).trim().split(/\s+/).filter(w => w !== "");
    const tWords = preProcess(targetText).trim().split(/\s+/).filter(w => w !== "");
    
    console.log("User words:", uWords);
    console.log("Target words:", tWords);
}

// Test cases
diffWords(
    "I hope you will consider [hành động - Ving].",
    "I hope you will consider [hành động – Ving]."
);

diffWords(
    "I hope you will consider [hành động-Ving].",
    "I hope you will consider [hành động – Ving]."
);

diffWords(
    "well-known",
    "well – known"
);
