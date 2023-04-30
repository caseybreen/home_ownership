## custom color schemes
cudb <- c("#49b7fc", "#ff7b00", "#17d898", "#ff0083", "#0015ff", "#e5d200", "#999999")
cud <- c("#D55E00", "#56B4E9", "#009E73", "#CC79A7", "#0072B2", "#E69F00", "#F0E442", "#999999")

## library packages 
library(data.table)
library(tidyverse)
library(here)
library(ggrepel)
library(cowplot)
library(socviz)
library(broom)
library(fixest)
library(gt)
library(LexisPlotR)
library(RColorBrewer)
library(ipumsr)
library(gompertztrunc)


## custom functions 

## Source .Rmd 

source_rmd = function(file, ...) {
  tmp_file = tempfile(fileext=".R")
  on.exit(unlink(tmp_file), add = TRUE)
  knitr::purl(file, output=tmp_file, quiet = T)
  source(file = tmp_file, ...)
}