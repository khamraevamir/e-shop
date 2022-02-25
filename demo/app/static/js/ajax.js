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
        
        
    
        $.ajax({
            url:url,
            type:'POST',
            data:{cart_id},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                // $('.cart_parent').load( ' .cart_child ')
                alert('Продукт изменен')
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
        console.log(quantity)

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
                // $('.cart_parent').load( ' .cart_child ')
                console.log('minus')
            },

            error: (msg)=> {
                console.log(msg)
            }
        }) 
    
    
         
        
    })
})