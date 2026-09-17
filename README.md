# PS-26189 Realistic Cross-Case Investigation Dataset

Synthetic 25-case dataset for demonstrating heterogeneous criminal-investigation ingestion and cross-case entity resolution.

The source evidence does not contain a list identifying which cases belong to the same network. Possible cross-case relationships must be inferred from repeated observations such as phone numbers, device identifiers, bank-account numbers, vehicle registrations, aliases/name variants, communications, transactions, locations and other contextual evidence.

Included sources: FIR records and legal sections, CDRs, financial transactions, surveillance logs, intelligence reports, social-media/OSINT, criminal-history context and case metadata.

Legal sections are retained as case context. A common legal section is not a network link by itself.

The dataset is synthetic and must not be represented as operational police data.
