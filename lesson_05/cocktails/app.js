//line 12 const d
const getIt = ()=>{
  let userInput = document.getElementById('userInput').value

  console.log(userInput)

  fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${userInput}`)
  .then(res => res.json()) // parse response as JSON
  .then(data => {
    console.log(...data.drinks)
    for(const d of data.drinks){

      if(d.strDrink === userInput){
        document.getElementById("name").innerText = userInput
        document.getElementById("instructions").innerText = d.strInstructions
      }
    }
  })
  .catch(err => {
      console.log(`error ${err}`)
  });


  }