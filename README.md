# l10n_ni_community

Localización contable para **Nicaragua**, compatible con **Odoo 17.0 Community**.

Nicaragua no cuenta con una localización contable oficial en el core de Odoo — este módulo busca cubrir ese vacío con una base contable completa y probada contra una instancia real de Odoo 17.

## Características

### Plan de cuentas
- 30 cuentas contables con códigos de 4 dígitos, organizadas en 10 grupos según NIIF para PYMES.
- Prefijos técnicos de cuentas (banco, caja, transferencias) configurados sobre el rango libre 1107–1199.

### Identificación de contactos
- Tipos de identificación: RUC, Cédula, Pasaporte (`l10n_latam.identification.type`).
- Validación de formato y dígito verificador:
  - Cédula: 13 dígitos + 1 letra, con verificación de la letra final mediante algoritmo módulo 23.
  - RUC persona natural: mismo formato y validación que la Cédula (en Nicaragua, el RUC de persona natural es su número de Cédula).
  - RUC jurídico: "J" + 13 dígitos (sin dígito verificador, ya que no existe un algoritmo público verificado para este formato).

### Impuestos
| Impuesto | Tasa | Uso |
|---|---|---|
| IVA por Ventas | 15% | Ventas |
| Exento Local | 0% | Ventas |
| Exportaciones | 0% | Ventas |
| Retenciones IR Proveedores | -2% | Compras (bienes/servicios en general) |
| Retención IR Servicios Profesionales | -10% | Compras |
| Retenciones IR Alquileres | -10% | Compras |

Todos los impuestos incluyen su reparto contable completo (base/impuesto para factura y nota de crédito).

### Posiciones fiscales
- **Nacional**: sin sustitución, aplica a clientes/proveedores en Nicaragua.
- **Exportación**: sustituye automáticamente el IVA 15% por el impuesto de exportación al 0% cuando el cliente no es de Nicaragua.

### Datos de compañía
- País fiscal configurado como Nicaragua.
- Etiqueta de identificación fiscal ("RUC") en los reportes PDF de factura.

## Instalación

1. Clona este repositorio dentro de tu `addons_path` de Odoo 17 (junto a la carpeta contenedora del módulo, no dentro de ella).
2. Instala el módulo `l10n_ni_community` desde Apps.
3. Crea o edita una compañía con **País = Nicaragua**.
4. Ve a Contabilidad y aplica la plantilla fiscal **Nicaragua**.

### Dependencias
- `account`
- `l10n_latam_base`

## Alcance actual y pendientes

**Completado:**
- Base contable (plan de cuentas, impuestos, posiciones fiscales, identificación).
- Formato de factura con campos requeridos por la DGI (RUC, desglose de IVA, nombre comercial).

**Fuera de alcance / configuración manual del usuario:**
- Prefijo de numeración de diarios (configurar en Contabilidad → Configuración → Diarios).
- Leyenda de autorización en pie de página (configurar en Ajustes → Compañías → Pie de página de reportes).

**Pendiente:**
- Casillas fiscales (`tag_ids`) para generar automáticamente la declaración de impuestos ante la DGI — actualmente el contador debe extraer los montos manualmente de los libros contables.
- Facturación electrónica DGI.

## Licencia

LGPL-3. Ver [LICENSE](LICENSE).
