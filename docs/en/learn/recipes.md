# Recipes

This section provides practical examples of using this library and code snippets.

## Data Analysis

In data analysis workflows, converting column names to a consistent format, such as [`snake`][textcase.snake],
can significantly simplify access to data and simplify its manipulation:

=== ":simple-python: analysis.py"

    ```py hl_lines="5 9" linenums="1"
    --8<-- "docs/.snippets/recipes/analysis/analysis.py"
    ```

=== ":fontawesome-solid-file-csv: input.csv"

    ```csv hl_lines="1" linenums="1"
    --8<-- "docs/.snippets/recipes/analysis/input.csv"
    ```

=== ":fontawesome-solid-file-csv: output.csv"

    ```csv hl_lines="1" linenums="1"
    --8<-- "docs/.snippets/recipes/analysis/output.csv"
    ```

By converting column names to a more accessible format,
you can later access data using `#!py row["user_id"]` instead of `#!py row["User::Id"]`.
This approach simplifies the syntax and improves code readability, making it easier to work with the data.

## Filenames Conversion

Different operating systems, such as Windows, macOS, and Linux, have distinct rules governing filenames.
Issues can arise from spaces, special characters, and case sensitivity when sharing files across platforms.
Converting filenames to a standardized format, such as [`kebab`][textcase.kebab], enhances compatibility
and minimizes the risk of errors when accessing files in various environments.

Consider the following example filenames that users might upload to a web application for conversion
into different file formats (e.g., Markdown to PDF, CSV to Excel):

--8<-- "docs/.snippets/recipes/filenames/filenames.md"

For instance, the filename `#!py "TODO #3 (Draft).md"` contains spaces and special characters, including `#!py "#"`,
which is interpreted as an **anchor** in URLs. This can result in broken links when generating download URLs.
For example, the URL `#!py "https://example.com/download/TODO%20#3%20(Draft).md"` may cause the browser
to misinterpret the link, preventing users from accessing the intended file.

To address this issue, you can use this library to convert filenames into a more compatible format:

=== ":simple-python: filenames.py"

    ```py hl_lines="13" linenums="1"
    --8<-- "docs/.snippets/recipes/filenames/filenames.py"
    ```

=== ":simple-markdown: result.md"

    --8<-- "docs/.snippets/recipes/filenames/result.md"

This conversion process ensures that filenames are safe for use across different platforms.
