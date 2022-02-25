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

document.querySelector('.cart_total').innerHTML = cart_total 



