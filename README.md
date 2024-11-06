# Quarto Crash Course

This repository contains source materials related to my live stream and Posit tutorial on Quarto.

Quarto is an open-source technical publication system that allows you to use a combination of Markdown & Python (or R, Julia, or Observable) code to easily produce websites, analytics dashboards, slideshows, and more.

## Installation

Check out [this link](https://quarto.org/docs/get-started/) to download the Quarto CLI (you also can typically install the CLI with pip in a virtual environment using `pip install quarto-cli`).

If you're using Windows, you'll want to make sure Quarto is added to your PATH (likely will be a checkbox option you can click when installing).

After you've installed the CLI, also use that same link to set up with your code editor. If you are using VS Code, you'll want to make sure that you have the [extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

## Docs

Here are some helpful resources

- https://quarto.org/docs/guide/ (General)
- https://quarto.org/docs/reference/ (for YAML keyword options)

A very helpful resource specific to Slideshows is [this presentation](https://quarto.org/docs/presentations/revealjs/demo/#/title-slide) and this corresponding [source code](https://github.com/quarto-dev/quarto-web/blob/main/docs/presentations/revealjs/demo/index.qmd)


## Resources

Data comes from [the Movie Database](https://www.themoviedb.org/) and was organized into a CSV via this [Kaggle Dataset](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies). 

Due to size issues with a GitHub repo, I've filtered by movies only with 1000+ reviews and saved it as [TMDB-Small.csv](./data/TMDB-Small.csv)
