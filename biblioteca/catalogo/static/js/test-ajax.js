//alert('pre hola mundo')
const getData = async()=>{
    try{
        const response = await fetch('./data');
        const data = await response.json();
        console.log(data) ;
        console.log('xd')
    } catch (error){
        console.log(error);
    }
};

const cargaInicial = async()=>{
    await getData();
};

window.addEventListener("load", async () =>{
    await cargaInicial();
});