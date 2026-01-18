# Xestor de Repostaxes

Aplicación en Python que permite rexistrar repostaxes dun vehículo, consultar o historial, calcular o gasto total e obter o consumo medio en L/100 km.  
O proxecto está estruturado de forma modular seguindo a arquitectura e requisitos indicada no enunciado da tarefa.

---
## Requisitos previos
- Python 3.10 ou superior
- Git (opcional)
---
### 1. Clonar ou descargar o proxecto.
Se usas Git:

```bash
git clone git@github.com:jabeceiro/xestor_repostaxes.git
cd xestor_repostaxes
```
Se non usas Git:  
 - Elixe "descargar ZIP"
### 2. Crear e activar o entorno virtual

```bash
python -m venv .venv
```

#### En Windows: 

```bash
.venv\Scripts\activate
```

#### En Linux/macOS

```bash
source .venv/bin/activate  
```
### 3. Instalar dependencias

```
pip install -r requirements.txt
```

### 4. Executar o programa

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
├── .gitignore            
├── main.py             # Punto de entrada da aplicación  
├── README.md           
└─── requirements.txt   # Dependencias externas   

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

- **Mostrar resumen.**    
  Mostra un resumo xeral das  repostaxes.  
     - Gasto total (€)
     - Kms totais percorridos (km)
     - Consumo total de combustible (L)
     - Consumo medio (L/100 km)  
  
- **Gardar datos.**  
  A lista de repostaxes almacenase en *data/datos.json*.  
  Para máis detalles, consulta o apartado **Como se gardan os datos**. 
  
## Exemplos de uso
### Inicio da aplicación  
```
╔════════════════════════════╗
║    XESTOR DE REPOSTAXES    ║
╚════════════════════════════╝
 1. Rexistrar repostaxe
 2. Mostrar historial
 3. Calcular gasto total
 4. Calcular consumo medio
 5. Mostrar resumen
 6. Gardar datos
 0. Saír
════════════════════════════════
Escolle unha opción:

```
---
### Rexistrar unha repostaxe
```
════════════════════════════════
Escolle unha opción: 1

========================================
          REXISTRAR REPOSTAXE
========================================
Data [2026-01-18]: 2026-01-17
Litros: 45
Prezo por litro (€): 1.27
Quilometraxe: 24500

✅ Repostaxe rexistrada correctamente.

```
### Mostrar historial

```
════════════════════════════════
Escolle unha opción: 2

==================================================
             HISTORIAL DE REPOSTAXES
==================================================
Data           Litros      €/L         Km
--------------------------------------------------
2025-12-10      35.20     1.32      21000
2025-12-17      12.67     1.12      21450
2025-12-24      23.00     1.15      22000
2026-01-02      40.50     1.29      22620
2026-01-15      28.75     1.20      23210
2026-01-15      32.10     1.25      23840
2026-01-17      45.00     1.27      24500
```

### Calcular gasto total

```
════════════════════════════════
Escolle unha opción: 3

================================
      CALCULAR GASTO TOTAL
================================
Data inicio:       2025-12-10
Data fin:          2026-01-17
Gasto total:           270.98 €

```
### Calcular consumo medio

```
════════════════════════════════
Escolle unha opción: 4

========================================
         CALCULAR CONSUMO MEDIO
========================================
Data inicio:       2025-12-10
Data fin:          2026-01-17
Consumo medio:           6.21 L/100 km
```

### Mostrar resumen

```
════════════════════════════════
Escolle unha opción: 5

========================================
              RESUMO XERAL
========================================
Data inicio:         2026-01-17
Data fin:            2026-01-18
Gasto total:         111.47 €
Km totais:           378671 km
Litros totais:       81.67 L
Consumo medio:       0.02 L/100 km
```
### Gardar datos
```
════════════════════════════════
Escolle unha opción: 6

✅ Datos gardados.

```

### Saír da aplicación
```
════════════════════════════════
Escolle unha opción: 0

Saíndo da aplicación...
Ata logo!

```
---
## 💾 Como se gardan os datos
As repostaxes almacenanse nun ficheiro JSON coa seguinte estructura:

```Json
[
    {
        "data": "2024-01-10",
        "litros": 45.2,
        "prezo_litro": 1.59,
        "kilometraxe": 123450
    }
]
```

A aplicación utiliza un ficheiro JSON situado en *data/datos.json* para almacenar o historial de repostaxes.  

É importante ter en conta:  
- Os datos non se gardan automaticamente cada vez que se engade unha repostaxe.  
- As novas entradas mantéñense en memoria mentres a aplicación está en execución.
- O usuario debe seleccionar a opción “6. Gardar datos” no menú para escribir os cambios no ficheiro JSON.
- Si se sale da aplicación, mediante a opción "0. Saír", e hai repostaxes sen gardar, gardanse.

Este comportamento evita estar escribindo constantemente no ficheiro cada vez que se rexistra unha repostaxe.

É importante ter en conta:

- As novas entradas non se gardan automaticamente no momento de rexistralas.

- Os datos mantéñense en memoria mentres a aplicación está en execución.

- O usuario pode gardar manualmente en calquera momento mediante a opción “6. Gardar datos”.

- Se o usuario sae da aplicación mediante a opción “0. Saír” e existen cambios pendentes, os datos gárdanse automaticamente antes de pechar.

- O menú mostra un asterisco (*), no título e na opción 6, cando hai cambios sen gardar.
  
```
╔════════════════════════════╗  
║    XESTOR DE REPOSTAXES  * ║  
╚════════════════════════════╝  
 1. Rexistrar repostaxe
 2. Mostrar historial
 3. Calcular gasto total
 4. Calcular consumo medio
 5. Mostrar resumen
 6. Gardar datos *
 0. Saír
════════════════════════════════
Escolle unha opción:
 ```
Este comportamento evita escribir no ficheiro cada vez que se rexistra unha repostaxe e garante que non se perda información, mantendo un equilibrio entre eficiencia e seguridade.

---

### Autor
Juan Antonio Beceiro Carro
### Licenza
MIT