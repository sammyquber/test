var menulist = document.getElementById("menulist");

    menulist.style.maxHeight = "0px";

    function togglemenu(){
        if
        (menulist.style.maxHeight == "0px")
        {
            menulist.style.maxHeight = "230px";
        }
        else
        {
            menulist.style.maxHeight = "0";
        }
    }

const toggle = document.getElementById('togglemenu()');
const nav = document.getElementById('nav');
toggle.addEventListener('click', () => {
    nav.classList.toggle('active')
});
