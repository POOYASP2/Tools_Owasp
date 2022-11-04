const jq_src = document.createElement('script');
jq_src.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
jq_src.addEventListener('load',()=>{
    $(document).ready(function() {
        document.title = 'blah';
    });
});

document.head.appendChild(jq_src);
