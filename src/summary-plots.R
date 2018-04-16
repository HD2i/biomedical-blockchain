library(ggplot2)
library(ggthemes)
library(dplyr)
library(forcats)
library(htmltab)

markdown.url = 'https://github.com/HD2i/biomedical-blockchain/blob/master/README.md'
# This function won't load images, so they appear as missing
# since actually missing values are encoded as a '-'
# we interpret missing here to mean there is an image icon
x = htmltab(markdown.url, fillNA = 'ICON')

ggplot(x, aes(x=fct_infreq(factor(Category)))) + geom_bar(fill = '#1e656d', width = 0.5) + 
  scale_fill_ptol() +
  theme_minimal(base_size = 14) + 
  theme(axis.text.x=element_text(angle=45,hjust=1), axis.title.x=element_blank())