
// 祝日の定数
const holidays = ["正月","成人の日","建国記念日","天皇誕生日","春分の日","昭和の日","憲法記念日","みどりの日","こどもの日","海の日","山の日","敬老の日","秋分の日","スポーツの日","文化の日","勤労感謝の日"]

// 順番通りに表示する
for (let i = 0; i <= holidays.length; i++) {
    console.log(holidays[i]);
  }
  
  let i = 0; 

// 変数numの値が0以外である間、変数numの値を出力し続ける
while (i < holidays.length) {
    console.log(holidays[i]);
    i++;
}
