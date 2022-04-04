
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





let memory_boxes = document.querySelectorAll('.memory_box')

for(let box of memory_boxes){
   
    box.addEventListener('click', ()=> {
        box.classList.add('active')
        console.log('ok')
     
    })
}





if(document.querySelector('.addProductColor') !== null){
    let addProductColor = document.querySelector('.addProductColor')
    let addProductColorContainer = document.querySelector('.addProductColorContainer')
    
    addProductColor.addEventListener('click', ()=> {
    
        if(addProductColor.innerHTML == 'Отменить'){
            addProductColorContainer.classList.add('d-none')
            addProductColor.className = 'btn btn-green rounded-1 addProductColor'
            addProductColor.innerHTML = 'Добавить цвет' 
        } else {
            addProductColorContainer.classList.remove('d-none')
            addProductColor.className = 'btn btn-grey rounded-1 addProductColor'
            addProductColor.innerHTML = 'Отменить'
        }
    
    
    })
    
    
}




if(document.querySelector('.addImage') !== null){
    let addImage = document.querySelector('.addImage')
    let inputFileContainer = document.querySelector('.inputFileContainer')

 


    addImage.addEventListener('click', (e)=> {


       

        let box = document.createElement('div')
        box.className = 'd-flex w-50'

        let input = document.createElement('input')
        input.setAttribute('type', 'file')
        input.setAttribute('name', 'image[]')
        input.className = 'input'

        // let btn = document.createElement('button') 
        // btn.className = 'btn btn-green rounded-1 ml-2'
        // btn.innerHTML = 'Добавить'

        let btnRemove = document.createElement('button') 
        btnRemove.className = 'btn btn-grey rounded-1 ml-2'
        btnRemove.innerHTML = 'Удалить'
        btnRemove.setAttribute('type', 'button')

        btnRemove.addEventListener('click', (e)=> {
            let parent = e.target.parentElement
            inputFileContainer.removeChild(parent)
            
        })

        box.appendChild(input)
        // box.appendChild(btn)
        box.appendChild(btnRemove)
        

        inputFileContainer.appendChild(box)

        if(inputFileContainer.querySelector('.btn-blue').classList.contains('d-none')){
            inputFileContainer.querySelector('.btn-blue').classList.remove('d-none')
        }
})

}


// // Table 
// let tableColors = document.querySelectorAll('.tableColors')



// // Select
// let selectColors = document.querySelectorAll('.colorsSelect')

// let colorsSelectContainer = document.querySelector('.colorsSelectContainer')


// let result = selectColors.length - tableColors.length - 1 



// selectColors.forEach((value, index) => {
//     if(result < index){
//         colorsSelectContainer.removeChild(value)
//     }
// })




