localStorage.setItem('count', 1)
getItem = 
document.querySelector("#displayCount").innerHTML = localStorage.
getItem('count')

//const getStr = localStorage.getItem('count')

document.querySelector('#add').addEventListener('click', addOne)
document.querySelector('#sub').addEventListener('click', subtractOne)
document.querySelector('#reset').addEventListener('click', resetLocal)

function addOne(){
    getStr = localStorage.getItem('count')
    total = Number(getStr) + 1;
    localStorage.setItem('count', total)
    document.querySelector("#displayCount").innerHTML = 
    localStorage.getItem('count')
}

function subtractOne(){
  getStr = localStorage.getItem('count')
  total = Number(getStr) - 1;
  localStorage.setItem('count', total)
  document.querySelector("#displayCount").innerHTML = 
  localStorage.getItem('count')
}

function resetLocal(){
  localStorage.setItem('count', 0)
  document.querySelector("#displayCount").innerHTML = 
  localStorage.getItem('count')
}
console.log(getStr)