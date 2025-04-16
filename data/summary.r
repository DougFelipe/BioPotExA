library(readxl)
library(dplyr)
library(tidyverse)
database <- read_excel("database.csv")
database_hadegDB <- read_excel("database_hadegDB.xlsx")
database_toxcsm <- read_excel("database_toxcsm.xlsx")




sortu <- function(df) {
  sorted_unique <- sort(unique(df))
  return(sorted_unique)
}

summary(database)


str(database)


dim(database)

table(database)

library(skimr)
skim(database)

library(Hmisc)
describe(database)

#Gerando SUPPLEMENTARY TABLE
###########
# Filtrar as colunas desejadas
suptablebrpp <- database %>%
  select(compoundname, ko, cpd, referenceAG) %>%
  distinct() # Manter apenas valores únicos

suptabletox <- database_toxcsm %>%
  select(SMILES,cpd,ChEBI) %>%
  distinct() # Manter apenas valores únicos

teste <- full_join(suptabletox,suptablebrpp, by = "cpd")


# Ajustar o dataframe para evitar repetições
new_dataframe <- database %>%
  group_by(compoundname) %>%
  summarise(
    ko = paste(unique(ko), collapse = ", "),
    cpd = paste(unique(cpd), collapse = ", "),
    referenceAG = paste(unique(referenceAG), collapse = ", ")
  ) %>%
  ungroup()

# Visualizar as primeiras linhas do novo dataframe
head(new_dataframe)


# Ajustar o dataframe para evitar repetições
new_dataframe <- teste %>%
  group_by(compoundname) %>%
  summarise(
    ko = paste(unique(ko), collapse = ", "),
    cpd = paste(unique(cpd), collapse = ", "),
    referenceAG = paste(unique(referenceAG), collapse = ", "),
    SMILES = paste(unique(SMILES), collapse = ", "),
    ChEBI = paste(unique(ChEBI), collapse = ", ")
  ) %>%
  ungroup()

# Visualizar as primeiras linhas do novo dataframe
head(new_dataframe)


# Instalar e carregar o pacote readr (se necessário)
install.packages("readr")
library(readr)

# Salvar o dataframe em um arquivo TSV
write_tsv(new_dataframe, "suptable.tsv")

# O arquivo será salvo no diretório de trabalho atual
