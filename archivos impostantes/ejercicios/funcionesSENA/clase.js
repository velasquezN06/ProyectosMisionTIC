class VentaTiquetes{
  constructor(){
    this.clientes = [];
    this.compra =[];
    this.pelicula =[];
  }
  registrarClientes(id,nombre,apellidos,edad){
    this.clientes[id]={id,nombre,apellidos,edad}
  }
  consultarCliente(id){
    return this.clientes[id];
  }
  
  registrarCompra(codigo,tiquetes,silla,pelicula){
     this.compra[codigo]={codigo,tiquetes,silla,pelicula}
  }
  consultarCompra(codigo){
     return this.compra[codigo];
  }
  
  registrarpelicula(id){
    const cliente = this.consultarCliente(id)
    const compra = this.consultarCompra(codigo)
    
  	this.pelicula[id]={
      compra:compra.codigo,
      compra:compra.tiquetes,
      compra:compra.silla,
      compra:compra.pelicula,
      
      
       }
  } 
  consultarpelicula(id){
    return this.pelicula[id];
  }
}
const ventaTiquetes = new VentaTiquetes

ventaTiquetes.registrarClientes(12,"nolberto","velasquez","15")
ventaTiquetes.registrarCompra(888,"2","12B","ben10")


ventaTiquetes.consultarpelicula()