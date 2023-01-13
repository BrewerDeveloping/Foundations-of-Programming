document.querySelector('#check').addEventListener('click', checkDay)


function checkDay() {
  

  const day = document.querySelector('#day').value
  let weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] 
  var result = ""

  if (weekday === day) {
    let result = "Weekday!"
  }


  document.querySelector('#placeToPutResult').innerText = let = result

}