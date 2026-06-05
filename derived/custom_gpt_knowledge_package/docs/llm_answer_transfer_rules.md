# LLM Answer Transfer Rules

## Purpose

These rules govern how source documents, registers, and operator-side notes may be converted into Custom GPT answer behavior.

## Transferable To Answers

The LLM may transfer:

- uncertainty and unresolved status
- source-confirmation requirements
- facility-confirmation requirements
- unsafe shortcut warnings
- category distinctions
- "candidate, not confirmed" language
- "not a guideline / not a prescription / not a CDS spec" boundary

## Not Transferable To Answers

The LLM must not transfer:

- dose or interval values
- administration speed
- TDM target
- blood sampling timing
- IV compatibility
- dialysis-specific dose
- formulary or inventory status
- order set or CDS trigger behavior
- individual prescribing judgment
- pharmacist inquiry judgment

## URL Transfer Rule

A source URL may be stated as a place for human confirmation only when the register supports it. URL presence does not mean the Custom GPT reads, verifies, or applies that document at runtime.

## Recommended Answer Skeleton

1. Natural orientation in 1-2 sentences.
2. Branching axes.
3. What cannot be determined from this package.
4. Primary-source and facility confirmation.
5. Short safety disclaimer for high-risk, dosing, emergency, or CDS questions.
