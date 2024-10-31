Sistema de Gestión de Venta de Autos

#Objetivo: 
Desarrollar un sistema de gestión para una concesionaria de autos que permita
manejar la venta de autos, clientes, y servicios post-venta.

#Requerimientos:
 Clases:
  o Auto: Código VIN, marca, modelo, año, precio, estado (nuevo/usado), cliente.
  o Cliente: ID, nombre, apellido, dirección, teléfono.
  o Venta: ID, auto, cliente, fecha de venta, vendedor.
  o Servicio: ID, auto, tipo de servicio (mantenimiento, reparación), fecha, costo.
  o Vendedor: ID, nombre, apellido, comisiones.
  
 Operaciones:

  1. Registro de Autos: Permitir el registro de nuevos autos en el inventario.
  2. Registro de Clientes: Permitir el registro de nuevos clientes.
  3. Registro de Ventas: Permitir la venta de autos y asignar comisiones a los
  vendedores.
  4. Registro de Servicios: Permitir registrar servicios post-venta para los autos
  vendidos.
  5. Consulta de Autos Vendidos: Consultar los autos vendidos a un cliente
  específico.
  6. Consulta de Servicios: Consultar los servicios realizados a un auto
  específico.
  7. Reportes:
     Listar todas las ventas realizadas en un periodo de tiempo.
     Generar un reporte de ingresos totales por venta de autos y por
    servicios.
     Generar un reporte de los autos más vendidos por marca.

Dificultad Extra:
   Incluir validaciones: Verificar que los autos no puedan venderse dos veces. Los
  servicios deben estar asociados a autos ya vendidos.
   Implementar reportes: generar un gráfico de torta que muestre la distribución de
  ventas por marca, y un gráfico de líneas mostrando los ingresos mensuales.
  Operaciones adicionales (opcion de agregar alguna si consideran):
    1. Gestión de Inventario de Repuestos: Crear un módulo para manejar el inventario
    de repuestos y accesorios para autos, con opciones para registrar nuevas entradas,
    ventas y bajas por desgaste.
    2. Servicio de Garantía: Implementar un sistema para gestionar las garantías de los
    autos vendidos. Permitir registrar reclamos por garantía y las reparaciones
    realizadas bajo la misma.
    3. Evaluación de Autos Usados: Añadir un módulo para evaluar autos usados que los
    clientes quieren dar en parte de pago, con la posibilidad de registrar el auto en el
    inventario si se acepta.
    4. Ofertas y Descuentos: Implementar la capacidad de aplicar descuentos especiales
    a ciertos autos o promociones por tiempo limitado, y reflejar estos descuentos en
    las ventas.
    
Reportes adicionales:
   Reporte de Repuestos Vendidos: Generar un reporte que muestre los repuestos
  más vendidos, con un gráfico de barras comparando las ventas por mes.
   Estadísticas de Garantías: Listar todas las garantías reclamadas en un periodo,
  con detalles sobre el tipo de falla y el costo cubierto por la garantía.
   Informe de Descuentos Aplicados: Crear un reporte que muestre el total de
  descuentos aplicados en un periodo, desglosado por tipo de auto y promoción.
