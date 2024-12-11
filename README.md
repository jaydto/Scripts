# Gift Randomization Script

This project contains two Python scripts for randomizing gift exchanges. The scripts ensure fairness and randomness while adding some fun dynamics to the process.

## Features

1. **Unique Gift Pairing**
   - Each person gifts exactly one other person.
   - No one gives a gift to themselves.
   - Completely randomized pairings.

2. **Reciprocal Gift Pairing**
   - Each pair of people exchange gifts with one another.
   - Ensures fairness by forming reciprocal pairs.

3. **Reusability**
   - The classes can be reused with different lists of names.
   - Configurable for an odd or even number of participants.

## Scripts

### 1. `GiftRandomizer`

This script creates unique gift pairings where each person gives a gift to another without repeats or self-pairing.

#### Example Output:
- **Gift Pairs** : John will give a gift to Nancy Nancy will give a gift to Wanjahi Wanjahi will give a gift to Njuguna Njuguna will give a gift to Stephani Stephani will give a gift to Jamila Jamila will give a gift to John


### 2. `ReciprocalGiftRandomizer`

This script creates reciprocal gift pairings where each pair exchanges gifts with one another.

#### Example Output:
- **Reciprocal Gift Pairs**: John will give a gift to Nancy, and Nancy will give a gift to John Wanjahi will give a gift to Njuguna, and Njuguna will give a gift to Wanjahi Stephani will give a gift to Jamila, and Jamila will give a gift to Stephani


## Usage

### Prerequisites

- Python 3.6 or higher.

### Installation

1. Clone this repository or download the script files.
2. Navigate to the project directory.

### Running the Scripts

#### Run the Unique Gift Randomization:
```bash
make unique
make reciprocal
```

## Makefile

A simple Makefile is provided for convenience:

```makefile
.PHONY: unique reciprocal

unique:
	python3 gift_randomizer.py

reciprocal:
	python3 reciprocal_gift_randomizer.py

