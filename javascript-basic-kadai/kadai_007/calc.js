// 変数を指定
let num = Math.floor(Math.random() * 500)

// コンソールに表示させる
console.log(num);

// ３の倍数の場合
if (num % 3 === 0){
    console.log("3の倍数です");
}
// ５の倍数の場合
else if (num % 5 ===0){
    console.log("５の倍数です");
}
// ３と５の倍数の場合
if(num % 3 ===0 && num % 5 ===0){
    console.log("３と５の倍数です")
}
// それ以外の場合
else {
    console.log(num)
}