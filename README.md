
# agjaeger.github.io

This is the git repository for my website.

## Structure
* assets/			TLD for asset files
  * posts/			Post Specific Assets
  * site/			Non Post Specific Assets
* _posts/			Posts
* _pages/			Non Post Pages (excluding index)
* _includes/		HTML snippets to include
* _layouts			HTML layouts for liquid

## Includes
* footer.html		Footer of each page
* header.html		Header of each page
* head.html			Head of each page (contains links and stylesheets)
* image				Snippet for easier image embedding

## Layouts
* default.html		Simple, head -> header -> content -> footer
* post.html			Specific for posts

## TODO
* Convert css to scss
* Asset pipeline currently works for images, but lets get js to work as well
* Remove unnecessary code (e.g. disqus and twitter integration)



