#!/usr/bin/env python3

import os
import sys
import json


def count_books(directory):
    """
    Count the number of book files in the specified directory

    :param directory: Path to the books directory
    :return: Number of book files
    """
    # Supported book file extensions
    book_extensions = {".pdf", ".epub", ".mobi", ".djvu", ".cbr", ".cbz"}

    try:
        # Expand user path and get all files
        books_dir = os.path.expanduser(directory)

        # Count files with book extensions
        book_count = len(
            [
                f
                for f in os.listdir(books_dir)
                if os.path.isfile(os.path.join(books_dir, f))
                and os.path.splitext(f)[1].lower() in book_extensions
            ]
        )

        return book_count

    except Exception as e:
        # If there's an error (e.g., directory doesn't exist)
        sys.stderr.write(f"Error counting books: {e}\n")
        return 0


def main():
    # Default Books directory
    books_dir = "~/Books"

    # Get book count
    book_count = count_books(books_dir)

    # Create JSON output for Waybar
    output = {"text": f"{book_count} 📚", "tooltip": f"Books in {books_dir}"}

    # Print JSON-formatted output
    print(json.dumps(output))


if __name__ == "__main__":
    main()
