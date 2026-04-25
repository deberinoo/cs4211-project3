# Event-B Extraction Output: `doors.json`

This file is auto-generated from the provided Event-B JSON artefacts.

## Contexts

### Context: `doors_ctx3`

- Extends: doors_ctx2
- Sets: D
- Constants: org, dst

**Axioms**

| Label | Predicate |
|---|---|
| `axm1` | org ∈ D → L |
| `axm2` | dst ∈ D → L |
| `axm3` | com = (org∼ ; dst) |


## Machines

### Machine: `doors_4`

- Refines: doors_3
- Sees: doors_ctx3

**Variables**

| Variable |
|---|
| `sit` |
| `dap` |
| `BLR` |
| `mCard` |
| `mAckn` |
| `mAccept` |
| `GRN` |
| `mPass` |
| `mOff_grn` |
| `mRefuse` |
| `RED` |
| `mOff_red` |

**Invariants (requirements candidates)**

| Label | Predicate |
|---|---|
| `inv1` | ran(dap) = mAccept ∪ mPass ∪ mOff_grn |
| `inv2` | mAccept ∩ (mPass ∪ mOff_grn) = ∅ |
| `inv4` | mPass ∩ mOff_grn = ∅ |
| `inv5` | red = mRefuse ∪ mOff_red |
| `inv6` | mRefuse ∩ mOff_red = ∅ |
| `inv8` | GRN ⊆ mAccept |
| `inv9` | RED ⊆ mRefuse |

**Initialisation (from `INITIALISATION` event)**

| Action | Assignment |
|---|---|
| `act1` | sit ≔ P×{outside} |
| `act2` | dap ≔ ∅ |
| `act4` | BLR ≔ ∅ |
| `act5` | mCard ≔ ∅ |
| `act6` | mAckn ≔ ∅ |
| `act7` | mAccept ≔ ∅ |
| `act3` | GRN ≔ ∅ |
| `act8` | mPass ≔ ∅ |
| `act9` | mOff_grn ≔ ∅ |
| `act10` | mRefuse ≔ ∅ |
| `act11` | RED ≔ ∅ |
| `act12` | mOff_red ≔ ∅ |

**Events (guards and actions)**

| Event | Params (ANY) | Guards (WHERE) | Actions (THEN) |
|---|---|---|---|
| `pass` | d | `grd11`: d∈mPass | `act11`: dap ≔ dap ⩥ {d}<br>`act1`: sit(dap∼(d)) ≔ dst(d)<br>`act2`: mAckn ≔ mAckn ∪ {d}<br>`act3`: mPass ≔ mPass∖{d} |
| `accept` | p, d | `grd1`: d↦p ∈ mCard<br>`grd11`: sit(p) = org(d)<br>`grd12`: p↦dst(d) ∈ aut<br>`grd13`: p ∉ dom(dap) | `act11`: dap(p) ≔ d<br>`act1`: mCard ≔ mCard ∖{d↦p}<br>`act2`: mAccept ≔ mAccept ∪ {d} |
| `refuse` | p, d | `grd12`: d↦p ∈ mCard<br>`grd11`: ¬(sit(p) = org(d) ∧ p↦dst(d) ∈ aut ∧ p∉dom(dap)) | `act1`: mCard ≔ mCard∖{d↦p}<br>`act2`: mRefuse ≔ mRefuse ∪ {d} |
| `off_grn` | d | `grd11`: d∈ mOff_grn | `act11`: dap ≔ dap ⩥ {d}<br>`act1`: mAckn ≔ mAckn ∪{d}<br>`act2`: mOff_grn ≔ mOff_grn∖{d} |
| `off_red` | d | `grd11`: d∈mOff_red | `act1`: mAckn ≔ mAckn ∪ {d}<br>`act2`: mOff_red ≔ mOff_red∖{d} |
| `CARD` | p, d | `grd11`: p ∈ P<br>`grd12`: d ∈ D∖BLR | `act11`: BLR ≔ BLR ∪ {d}<br>`act12`: mCard ≔ mCard ∪ {d↦p} |
| `ACKN` | d | `grd11`: d ∈ mAckn | `act11`: BLR ≔ BLR∖{d}<br>`act12`: mAckn ≔ mAckn∖{d} |
| `ACCEPT` | d | `grd11`: d∈mAccept | `act11`: GRN ≔ GRN ∪ {d} |
| `REFUSE` | d | `grd11`: d∈mRefuse | `act11`: RED ≔ RED ∪ {d} |
| `PASS` | d | `grd11`: d∈GRN | `act11`: GRN ≔ GRN∖{d}<br>`act12`: mPass ≔ mPass ∪ {d}<br>`act13`: mAccept ≔ mAccept ∖{d} |
| `OFF_GRN` | d | `grd11`: d∈GRN | `act11`: GRN ≔ GRN ∖ {d}<br>`act12`: mOff_grn ≔ mOff_grn ∪ {d}<br>`act13`: mAccept ≔ mAccept∖{d} |
| `OFF_RED` | d | `grd11`: d∈RED | `act11`: RED ≔ RED ∖ {d}<br>`act12`: mOff_red ≔ mOff_red ∪ {d}<br>`act13`: mRefuse ≔ mRefuse ∖ {d} |
