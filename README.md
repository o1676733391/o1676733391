<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* Add any additional styling here */
    </style>
</head>
<body>
    <h1>Welcome to Our Project</h1>
    <p>This is an example of using <picture> tags for dark/light mode icons.</p>
    <picture>
        <source srcset="assets/icons/icon.svg" media="(prefers-color-scheme: dark)">
        <img src="assets/icons/icon.svg" style="filter: invert(1); vertical-align: -2px;" alt="Icon">
    </picture>
    <p>More content here...</p>
</body>
</html>