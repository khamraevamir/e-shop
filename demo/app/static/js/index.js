
$(document).ready(function() {
    $('.category').select2();
});


$(document).ready(function() {
    $('.colors').select2();
});

let codify = () => {


    return({
        createModal: (name) => {
            let btns = document.querySelectorAll(`.${name}`)
            let modal = document.querySelector(`#${name}`)

            for(let btn of btns){
                btn.addEventListener('click', ()=> {
                    modal.classList.toggle('d-none')
                })
            }
            
        },
       
    })
}



let cart_items = document.querySelectorAll('.cart_price')
let cart_total = 0

for(let item of cart_items){

    let parent = item.parentElement.parentElement
    let quantity = Number(parent.querySelector('.input').value)
    let result = Number(item.innerHTML) * quantity

    cart_total += result
}

// document.querySelector('.cart_total').innerHTML = cart_total 
// document.querySelector('.hidden_total').value = cart_total 



let memoryCreateModal = () => {
    let parent = window.event.target.parentElement.parentElement
    console.log(parent)
    parent.querySelector('.product_memory_create_modal').classList.add('d-block')
}


let memoryEditModal = () => {
    let parent = window.event.target.parentElement.parentElement
    console.log(parent)
    parent.querySelector('.product_memory_edit_modal').classList.add('d-block')
}



let moreBtns = document.querySelectorAll('.moreProductColor')



for(let btn of moreBtns){
    btn.addEventListener('click', (e)=> {

        let moreBoxContainer = e.target.parentElement.querySelector('.moreBoxContainer')
       
        let box = document.querySelector('.moreBox')
        let clone = box.cloneNode(true)

        clone.classList.remove('d-none')

        moreBoxContainer.appendChild(clone)

        

    
    })
}