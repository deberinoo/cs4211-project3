# Event-B Extraction Output: `car.json`

This file is auto-generated from the provided Event-B JSON artefacts.

## Contexts

### Context: `cd`

- Extends: -
- Sets: -
- Constants: d

**Axioms**

| Label | Predicate |
|---|---|
| `axm1` | d>0 |


### Context: `COLOR`

- Extends: -
- Sets: Color
- Constants: green, red

**Axioms**

| Label | Predicate |
|---|---|
| `axm1` | partition(Color, {green}, {red}) |


### Context: `SENSOR`

- Extends: -
- Sets: Sensor
- Constants: on, off

**Axioms**

| Label | Predicate |
|---|---|
| `axm1` | partition(Sensor, {on}, {off}) |


## Machines

### Machine: `m3`

- Refines: m2
- Sees: cd, COLOR, SENSOR

**Variables**

| Variable |
|---|
| `a` |
| `b` |
| `c` |
| `ml_tl` |
| `il_tl` |
| `il_pass` |
| `ml_pass` |
| `A` |
| `B` |
| `C` |
| `ML_OUT_SR` |
| `ML_IN_SR` |
| `IL_OUT_SR` |
| `IL_IN_SR` |
| `ml_out_10` |
| `il_out_10` |
| `ml_in_10` |
| `il_in_10` |

**Invariants (requirements candidates)**

| Label | Predicate |
|---|---|
| `inv1` | IL_IN_SR = on ⇒ A>0 |
| `inv2` | IL_OUT_SR = on ⇒ B>0 |
| `inv3` | ML_IN_SR = on ⇒ C>0 |
| `inv4` | ml_out_10 = TRUE ⇒ ml_tl=green |
| `inv5` | il_out_10 = TRUE ⇒ il_tl = green |
| `inv6` | IL_IN_SR = on ⇒ il_in_10 = FALSE |
| `inv7` | IL_OUT_SR = on ⇒ il_out_10 = FALSE |
| `inv8` | ML_IN_SR = on ⇒ ml_in_10 = FALSE |
| `inv9` | ML_OUT_SR = on ⇒ ml_out_10 = FALSE |
| `inv10` | il_in_10 = TRUE ∧ ml_out_10 = TRUE ⇒ A = a |
| `inv11` | il_in_10 = FALSE ∧ ml_out_10 = TRUE ⇒ A = a+1 |
| `inv12` | il_in_10 = TRUE ∧ ml_out_10 = FALSE ⇒ A = a−1 |
| `inv13` | il_in_10 = FALSE ∧ ml_out_10 = FALSE ⇒ A = a |
| `inv14` | il_in_10 = TRUE ∧ il_out_10 = TRUE ⇒ B=b |
| `inv15` | il_in_10 = TRUE ∧ il_out_10 = FALSE ⇒ B = b+1 |
| `inv16` | il_in_10 = FALSE ∧ il_out_10 = TRUE ⇒ B = b−1 |
| `inv17` | il_in_10 = FALSE ∧ il_out_10 = FALSE ⇒ B=b |
| `inv18` | il_out_10 = TRUE ∧ ml_in_10 = TRUE ⇒ C=c |
| `inv19` | il_out_10 = TRUE ∧ ml_in_10 = FALSE ⇒ C=c+1 |
| `inv20` | il_out_10 = FALSE ∧ ml_in_10 = TRUE ⇒ C=c−1 |
| `inv21` | il_out_10 =FALSE ∧ ml_in_10 = FALSE ⇒ C=c |
| `inv22` | A=0 ∨ C=0 |
| `inv23` | A+B+C ≤ d |
| `inv24` | A∈ℕ |
| `inv25` | B∈ℕ |
| `inv26` | C∈ℕ |

**Initialisation (from `INITIALISATION` event)**

| Action | Assignment |
|---|---|
| `act2` | a ≔ 0 |
| `act3` | b ≔ 0 |
| `act4` | c ≔ 0 |
| `act1` | ml_tl≔red |
| `act5` | il_tl≔red |
| `act6` | ml_pass≔1 |
| `act7` | il_pass≔1 |
| `act15` | ml_out_10 ≔ FALSE |
| `qct16` | il_out_10 ≔ FALSE |
| `act17` | ml_in_10 ≔ FALSE |
| `act18` | il_in_10 ≔ FALSE |
| `act8` | A ≔ 0 |
| `act9` | B ≔ 0 |
| `act10` | C ≔ 0 |
| `act11` | ML_IN_SR ≔ off |
| `act12` | ML_OUT_SR ≔ off |
| `act13` | IL_OUT_SR ≔ off |
| `act14` | IL_IN_SR ≔ off |

**Events (guards and actions)**

| Event | Params (ANY) | Guards (WHERE) | Actions (THEN) |
|---|---|---|---|
| `ML_out1` | - | `grd1`: ml_out_10= TRUE<br>`grd2`: a+b+1<d | `act1`: a≔a+1<br>`act2`: ml_pass≔1<br>`act3`: ml_out_10 ≔ FALSE |
| `ML_out2` | - | `grd1`: ml_out_10 = TRUE<br>`grd2`: a+b+1=d | `act1`: a≔a+1<br>`act2`: ml_tl≔red<br>`act3`: ml_pass≔1<br>`act4`: ml_out_10 ≔ FALSE |
| `IL_out1` | - | `grd1`: il_out_10 = TRUE<br>`grd2`: b>1 | `act1`: b≔b−1<br>`act2`: c≔c+1<br>`act3`: il_pass≔1<br>`act4`: il_out_10 ≔ FALSE |
| `IL_out2` | - | `grd1`: il_out_10 = TRUE<br>`grd2`: b=1 | `act1`: b≔b−1<br>`act2`: il_tl≔red<br>`act3`: c≔c+1<br>`act4`: il_pass≔1<br>`act5`: il_out_10 ≔ FALSE |
| `ML_tl_green` | - | `grd1`: ml_tl=red<br>`grd2`: a+b<d<br>`grd3`: c=0<br>`grd4`: il_pass=1<br>`grd5`: il_out_10 = FALSE | `act1`: ml_tl≔green<br>`act2`: il_tl≔red<br>`act3`: ml_pass≔0 |
| `IL_tl_green` | - | `grd1`: il_tl=red<br>`grd2`: 0<b<br>`grd3`: a=0<br>`grd4`: ml_pass=1<br>`grd5`: ml_out_10 = FALSE | `act1`: il_tl≔green<br>`act2`: ml_tl≔red<br>`act3`: il_pass≔0 |
| `ML_in` | - | `grd1`: ml_in_10 = TRUE<br>`grd2`: c>0 | `act1`: c ≔ c−1<br>`act2`: ml_in_10 ≔ FALSE |
| `IL_in` | - | `grd1`: il_in_10 = TRUE<br>`grd2`: 0 < a | `act1`: a ≔ a−1<br>`act2`: b ≔ b+1<br>`act3`: il_in_10 ≔ FALSE |
| `ML_OUT_ARR` | - | `grd1`: ML_OUT_SR = off<br>`grd2`: ml_out_10 = FALSE | `act1`: ML_OUT_SR ≔ on |
| `ML_IN_ARR` | - | `grd1`: ML_IN_SR = off<br>`grd2`: ml_in_10 = FALSE<br>`grd3`: C > 0 | `act1`: ML_IN_SR ≔ on |
| `IL_IN_ARR` | - | `grd1`: IL_IN_SR = off<br>`grd2`: il_in_10 = FALSE<br>`grd3`: A > 0 | `act1`: IL_IN_SR ≔ on |
| `IL_OUT_ARR` | - | `grd1`: IL_OUT_SR = off<br>`grd2`: il_out_10 = FALSE<br>`grd3`: B > 0 | `act1`: IL_OUT_SR ≔ on |
| `ML_OUT_DEP` | - | `grd1`: ML_OUT_SR = on<br>`grd2`: ml_tl = green | `act1`: ML_OUT_SR ≔ off<br>`act2`: ml_out_10 ≔ TRUE<br>`act3`: A ≔ A+1 |
| `ML_IN_DEP` | - | `grd1`: ML_IN_SR = on | `act1`: ML_IN_SR ≔ off<br>`act2`: ml_in_10 ≔ TRUE<br>`act3`: C ≔ C−1 |
| `IL_IN_DEP` | - | `grd1`: IL_IN_SR = on | `act1`: IL_IN_SR ≔ off<br>`act2`: il_in_10 ≔ TRUE<br>`act3`: A ≔ A−1<br>`act4`: B ≔ B+1 |
| `IL_OUT_DEP` | - | `grd1`: IL_OUT_SR = on<br>`grd2`: il_tl =  green | `act1`: IL_OUT_SR ≔ off<br>`act2`: il_out_10 ≔ TRUE<br>`act3`: B ≔ B−1<br>`act4`: C ≔ C+1 |
