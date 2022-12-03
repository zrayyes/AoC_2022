const text = await Deno.readTextFile("./input.txt");
let score_A = 0;
let score_B = 0;
for (const line of text.split(/\r?\n/)) {
    const opponent = line.charAt(0).charCodeAt(0) - "A".charCodeAt(0);
    const player = line.charAt(2).charCodeAt(0) - "X".charCodeAt(0);
    score_A += 1 + player + 3 * ((2 * opponent + player + 1) % 3);
    score_B += 1 + player * 3 + (3 + opponent + player - 1) % 3;
}

console.log(score_A)
console.log(score_B)