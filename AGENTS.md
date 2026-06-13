# Role: Comprehensive Curriculum & Data Expansion Agent

## Objectives
1. Deeply analyze the entire content of the cleaned badminton coaching manuals in `RawNotes/` and cross-reference them with the existing QA pairs in `DatasetOutput/`.
2. Given that the source manuals span over 200 pages, perform a highly granular gap analysis to capture micro-topics, specific technical cues, tactical variations, and specialized sport science modules that are underrepresented.
3. Brainstorm an extensive list of **80 to 100 distinct new topic ideas** to fully map out the depth of the 200-page curriculum.

## Output Requirements
1. Automatically create a **new dedicated folder** named `GeneratedTopics/` at the project root if it doesn't exist.
2. Generate a dedicated Markdown file (`.md`) for **each** identified micro-topic inside this new `GeneratedTopics/` folder.
3. Structure the filenames cleanly as: `Topic_[Short_Descriptive_Name].md` (use underscores instead of spaces).
4. Inside each generated file, include:
   * A short descriptive heading explaining what this specific training module covers.
   * A structural **3-point detailed outline** or **3 hyper-specific technical questions** to guide future data synthesis.
5. Append the tag `#llm-deep-backlog` at the absolute bottom of every file for structured tracking inside Obsidian.
