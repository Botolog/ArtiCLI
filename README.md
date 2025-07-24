# Knowledge Base Manager (KBM)

## Usage

The Knowledge Base Manager (KBM) is a command-line tool for managing articles and their associated data. It allows you to perform various operations such as loading, creating, editing, deleting, and searching articles.

### Available Commands

- `load [filename]`: Loads a JSON file containing article data.
- `show [option] [values]`: Displays articles based on the specified filter options. Options include:
  - `search`: Displays articles that contain the given search term in the title, content, or tags.
  - `tag`: Displays articles that contain at least one of the specified tags.
  - `tags`: Displays articles that contain all of the specified tags.
- `clear`: Clears the current article data.
- `save [filename]`: Saves the current article data to a JSON file.
- `create [id] [title]`: Creates a new article with the specified ID and title (optional).
- `delete [id]`: Deletes the article with the specified ID.
- `edit [id] [field] [new_value]`: Edits the specified field of the article with the given ID.
- `addtag [id] [tag_name] [tag_name]...`: Adds the specified tags to the article with the given ID.
- `remtag [id] [tag_name] [tag_name]...`: Removes the specified tags from the article with the given ID.
- `help [command_name]`: Displays the help information for the specified command or for all commands if no command is provided.

### Examples

- Load a JSON file:
  ```
  > load data.json
  ```
- Display articles that contain the search term "payment":
  ```
  > show search payment
  ```
- Display articles that contain the tags "checkout" and "email":
  ```
  > show tags checkout email
  ```
- Create a new article:
  ```
  > create 123 My Article
  ```
- Edit the title of an article:
  ```
  > edit 123 title "New Article Title"
  ```
- Add a tag to an article:
  ```
  > addtag 123 important
  ```
- Remove a tag from an article:
  ```
  > remtag 123 important
  ```
- Display help for the "show" command:
  ```
  > help show
  ```