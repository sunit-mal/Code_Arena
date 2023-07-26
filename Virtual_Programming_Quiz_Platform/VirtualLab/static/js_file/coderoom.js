document.querySelector('#a1').addEventListener('click', ()=> {
    document.querySelector('#input').className = "min";
    document.querySelector('.out').classList.add("minout");
    document.querySelector('.out').classList.remove("maxout");
})
document.querySelector('#a2').addEventListener('click', ()=> {
    document.querySelector('#input').className = "normal";
    document.querySelector('.out').classList.add("minout");
    document.querySelector('.out').classList.remove("maxout");
})
document.querySelector('#a3').addEventListener('click', ()=> {
    document.querySelector('#input').className = "max";
    document.querySelector('.out').classList.add("maxout");
    document.querySelector('.out').classList.remove("minout");
})