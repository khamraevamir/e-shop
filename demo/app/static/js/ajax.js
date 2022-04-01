$(function(){
    $('.addToCart').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let product = btn.attr('data-id')
            
    
        $.ajax({
            url:url,
            type:'POST',
            data:{product},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                $('.cart_parent').load( ' .cart_child ')
                alert('Продукт добавлен')
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})




$(function(){
    $('.cartPlus').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let cart_id = btn.attr('data-id')

        let input_parent = btn.parent().find('.cart_input_parent')
        
        
        
    
        $.ajax({
            url:url,
            type:'POST',
            data:{cart_id},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                input_parent.load(` .cart_input_child${cart_id} `)

                let cart_items = document.querySelectorAll('.cart_price')
                cart_total = 0

                for(let item of cart_items){

                    let parent = item.parentElement.parentElement
                    let quantity = 0
                    
                    if(item.id == cart_id){
                        quantity = Number(parent.querySelector('.input').value) + 1
                      
                    } else {
                        quantity = Number(parent.querySelector('.input').value)
                    }
                    let result = Number(item.innerHTML) * quantity

                    cart_total += result
                }

                console.log(cart_total)

                document.querySelector('.cart_total').innerHTML = cart_total 
                document.querySelector('.hidden_total').value = cart_total 

                

               
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})



$(function(){
    $('.cartMinus').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let cart_id = btn.attr('data-id')
        let quantity = btn.parent().find('.input').val()
        let input_parent = btn.parent().find('.cart_input_parent')

        if(quantity == 1){
            btn.parent().parent().parent().remove()
        }
      
        $.ajax({
            url:url,
            type:'POST',
            data:{cart_id, quantity},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                input_parent.load(` .cart_input_child${cart_id} `)
                
                let cart_items = document.querySelectorAll('.cart_price')
                cart_total = 0

                for(let item of cart_items){

                    let parent = item.parentElement.parentElement
                    let quantity = 0
                    
                    if(item.id == cart_id){
                        quantity = Number(parent.querySelector('.input').value) - 1
                      
                    } else {
                        quantity = Number(parent.querySelector('.input').value)
                    }
                    let result = Number(item.innerHTML) * quantity

                    cart_total += result
                }

                console.log(cart_total)

                document.querySelector('.cart_total').innerHTML = cart_total 
                document.querySelector('.hidden_total').value = cart_total 

               
            },

            error: (msg)=> {
                console.log(msg)
            }
        }) 
    
    
         
        
    })
})





// Edit produt color size




$(document).on("click",".productColorSizeEdit",function(){
    let btn = $(this)
    let token = $('[name = csrfmiddlewaretoken').val()
    let url = btn.attr('data-url')
    let id = btn.attr('data-id')
    let price = btn.parent().parent().find('.price_input').val()

    let price_input = btn.parent().parent().find('.price_input')

    let parentRefresh = $('.editParentRefresh')

    
  
   
    $.ajax({
        url:url,
        type:'POST',
        data:{id,price},
        headers:{
            'X-CSRFToken':token
        },


        success: (data)=>{
            price_input.val(data)
            btn.html('Изменено')
            btn.removeClass('btn-blue')
            btn.addClass('btn-green')

            setTimeout(()=> {
                btn.html('Изменить')
                btn.addClass('btn-blue')
                btn.removeClass('btn-green')
            },2000)
      
            parentRefresh.load(location.href + ` .editRefresh`)

            
        },

        error: (msg)=> {
            console.log(msg)
        }
    })  
    
})




$(function(){
    $('.productColorSizeAdd').on('click', function() {
      
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let id = btn.attr('data-id')

        let price = btn.parent().find('.productColorSizePrice')[1]
        let memory = btn.parent().find('.productColorSizeMemory')[1]

      
        price = price.value
        memory = memory.value
      
     
       
        $.ajax({
            url:url,
            type:'POST',
            data:{id,price,memory},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                console.log(data)
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})





