---

## 📁 Dataset 9: Preço de Carros Usados

### 📄 Arquivo
`used_cars_price.csv`

### 🎯 Objetivo
Prever **preço de revenda** (em R$) de carros usados com base em características do veículo, histórico e condição.

### 📊 Características
- **Registros:** 2.520
- **Features:** 25
- **Variável Alvo:** `price_brl` (preço em R$)
- **Tipo:** Regressão

### 📝 Variáveis

#### Características Básicas
- `car_id`: ID único
- `brand`: Marca (Toyota, Honda, Volkswagen, Chevrolet, Ford, Fiat, Hyundai)
- `model_year`: Ano do modelo (2010-2024)
- `mileage_km`: Quilometragem (5.000-250.000 km)
- `fuel_type`: Tipo de combustível (Gasolina, Etanol, Flex, Diesel, Híbrido, Elétrico)

#### Motor e Performance
- `engine_size_liters`: Tamanho do motor em litros (1.0-3.0)
- `horsepower`: Potência em cavalos (70-300)
- `transmission`: Transmissão (Manual, Automática, CVT, Automatizada)
- `drivetrain`: Tração (Dianteira, Traseira, 4x4)

#### Condição e Histórico
- `condition`: Condição geral (Excelente, Bom, Regular, Ruim)
- `previous_owners`: Donos anteriores (1-5)
- `accident_history`: Histórico de acidentes (Sem acidentes, 1 acidente leve, 2+ acidentes)
- `service_history`: Histórico de manutenção (Completo, Parcial, Sem histórico)

#### Features e Equipamentos
- `air_conditioning`: Ar condicionado (Sim/Não)
- `power_steering`: Direção hidráulica (Sim/Não)
- `power_windows`: Vidros elétricos (Sim/Não)
- `airbags_count`: Número de airbags (0-8)
- `abs_brakes`: Freios ABS (Sim/Não)

#### Acabamento e Extras
- `interior_material`: Material do interior (Tecido, Couro Sintético, Couro Legítimo)
- `sound_system`: Sistema de som (Básico, Premium, Multimídia)
- `sunroof`: Teto solar (Sim/Não)
- `parking_sensors`: Sensores de estacionamento (Sim/Não)

#### Documentação e Origem
- `warranty_months`: Garantia em meses (0-36)
- `imported`: Importado (Sim/Não)
- `color`: Cor (Prata, Preto, Branco, Vermelho, Azul, Cinza)

### 💡 Aplicação Prática
Precificação automática de veículos, avaliação de negociações, identificar boas oportunidades de compra.

---
