# Xestor de Repostaxes

Aplicación en Python que permite rexistrar repostaxes dun vehículo, consultar o historial, calcular o gasto total e obter o consumo medio en L/100 km.  
O proxecto está estruturado de forma modular seguindo a arquitectura indicada no enunciado.

---
## Instalación
```bash
python -m venv .venv
# En Windows: 
.venv\Scripts\activate
# En Linux
source .venv/bin/activate  

pip install -r requirements.txt

```

## Uso
```bash
python main.py
```
## 📁 Estrutura do proxecto

```txt
XESTOR_REPOSTAXES/  
├─app    
│  │           
│  ├── __init__.py      
│  ├── funciones.py     # Lóxica de negocio (validacións e cálculos)  
│  └── io.py            # Entrada/saída: menús, impresión e persistencia  
├── data/  
│   └── datos.json      # Ficheiro onde se gardan as repostaxes  
├── .gitignore          # Exclusión de carpetas e ficheiros  
├── main.py             # Punto de entrada da aplicación  
├── README.md           # Documentación do proxecto  
└─── requirements.txt   # Dependencias externas   
```

## Como executar o programa

1. Asegurate de ter instalado Python 3.10 ou superior
2. Clona o repositorio ou descarga os ficheros.
3. Instala as dependecias:
   
   ```bash
      pip install -r requirementas.txt
   ```
4. Executa o programa:

   ```bash
      python main.py
   ```
---
## Funcionalidades principais
- **Rexistar repostaxe**  
  Introduce data, litro, prezo por litro e quilometraxe.  
  A aplicación valida os datos antes de gardalos.
- **Mostrar historial.**  
  Lista todas as repostaxes rexistradas.
- **Calcular gasto total.**  
  Suma do custo de todas as repostaxes.
- **Calcular consumo medio.**  
  Cálculo de litros/100 km a partir dos kms percorridos.
- **Gardar datos.**  
  A lista de repostaxes almacenase en *data/datos.json*.  
  Para máis detalles, consulta o apartado **Como se gardan os datos**. 
  
## Exemplos de uso
### 1. Inicio da aplicación  
```
--- XESTOR DE REPOSTAXES ---
1. Rexistrar repostaxe
2. Amosar historial
3. Calcular gasto total
4. Calcular consumo medio
5. Gardar datos
6. Saír
Escolle unha opción:
```
---
### 2. Rexistrar unha repostaxe
```
--- Rexistrar repostaxe ---
Data [2025-01-17]: 2025-01-10
Litros: 45.3
Prezo por litro (€): 1.62
Quilometraxe: 152340
Repostaxe rexistrada correctamente.

```
💾 Como se gardan os datos
A aplicación utiliza un ficheiro JSON situado en data/datos.json para almacenar o historial de repostaxes.  
É importante ter en conta:  
- Os datos non se gardan automaticamente cada vez que se engade unha repostaxe.  
- As novas entradas mantéñense en memoria mentres a aplicación está en execución.
- O usuario debe seleccionar a opción “5. Gardar datos” no menú para escribir os cambios no ficheiro JSON.

- Se se sae da aplicación sen gardar, os cambios perderanse.

Este comportamento permite revisar, engadir ou modificar datos antes de confirmar o gardado definitivo.
---
### Autor
Juan Antonio Beceiro Carro
### Licenza
MIT