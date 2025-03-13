export const getPages = (current: number, total: number, onSides: number = 3) => {
    // pages
    let pages = [];
    // Loop through
    for (let i = 1; i <= total; i++) {
        // Define offset
        let offset = (i == 1 || total) ? onSides + 1 : onSides;
        // If added
        if (i == 1 || (current - offset <= i && current + offset >= i) ||
            i == current || i == total) {
            pages.push(i);
        } else if (i == current - (offset + 1) || i == current + (offset + 1)) {
            pages.push('...');
        }
    }
    return pages;
}