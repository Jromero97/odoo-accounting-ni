# l10n_ni_community

Accounting localization for **Nicaragua**, compatible with **Odoo 17.0 Community**.

Nicaragua does not have an official accounting localization in Odoo's core — this module aims to fill that gap with a complete accounting foundation, tested against a real Odoo 17 instance.

## Features

### Chart of accounts
- 30 accounts with 4-digit codes, organized into 10 groups following NIIF for SMEs.
- Technical account prefixes (bank, cash, transfers) configured over the free 1107–1199 range.

### Contact identification
- Identification types: RUC, Cédula, Passport (`l10n_latam.identification.type`).
- Format and check-digit validation:
  - Cédula: 13 digits + 1 letter, with the final letter verified using a modulo-23 algorithm.
  - RUC (natural person): same format and validation as the Cédula (in Nicaragua, a natural person's RUC is their Cédula number).
  - RUC (legal entity): "J" + 13 digits (no check digit, since no verified public algorithm exists for this format).

### Taxes
| Tax | Rate | Use |
|---|---|---|
| Sales VAT | 15% | Sales |
| Local Exempt | 0% | Sales |
| Exports | 0% | Sales |
| Vendor IR Withholding | -2% | Purchases (general goods/services) |
| Professional Services IR Withholding | -10% | Purchases |
| Rentals IR Withholding | -10% | Purchases |

All taxes include their full accounting distribution (base/tax for both invoice and credit note).

### Fiscal positions
- **Domestic**: no substitution, applies to customers/vendors in Nicaragua.
- **Export**: automatically replaces the 15% VAT with the 0% export tax when the customer is not in Nicaragua.

### Company data
- Fiscal country set to Nicaragua.
- Fiscal identification label ("RUC") on invoice PDF reports.

## Installation

1. Clone this repository into your Odoo 17 `addons_path` (next to the module's containing folder, not inside it).
2. Install the `l10n_ni_community` module from Apps.
3. Create or edit a company with **Country = Nicaragua**.
4. Go to Accounting and apply the **Nicaragua** fiscal chart template.

### Dependencies
- `account`
- `l10n_latam_base`

## Current scope and pending work

**Completed:**
- Accounting foundation (chart of accounts, taxes, fiscal positions, identification).
- Invoice formatting with DGI-required fields (RUC, VAT breakdown, trade name).

**Out of scope / manual user configuration:**
- Journal numbering prefix (configure in Accounting → Configuration → Journals).
- Authorization legend in the report footer (configure in Settings → Companies → report footer).

**Pending:**
- Tax grid tags (`tag_ids`) to automatically generate the tax return for the DGI — accountants currently need to pull the figures manually from the books.
- DGI electronic invoicing.

## License

LGPL-3. See [LICENSE](LICENSE).
