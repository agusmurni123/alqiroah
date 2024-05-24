const menu = document.querySelector('.menu');
const tbl = document.querySelector('.fa-bars');
tbl.addEventListener('click',function(){
    menu.classList.toggle('menuaktive');
});

const viewIkon = document.querySelector('.fa-eye');
const hasilView = document.querySelector('.view');
let count = 0;

viewIkon.addEventListener('click',function(){

    const postID = "{{redaksi.id}}";

    fetch(`/view_blogs/?view_id=${postID}`)
    .then(response => response.json())
    .then(data => {
            if (data.success) {
                if(viewIkon.classList.contains('viewer')){
                    viewIkon.classList.remove('viewer');
                    count = 0;
                } else{
                    viewIkon.classList.add('viewer');
                    count = data.views;
                }

                hasilView.innerHTML= count;
            } else{
                console.error('gagal view post:',data.error);
            }
        })
        .catch(error =>{
        console.error('Error viewing post:',error);
        });
    });
    