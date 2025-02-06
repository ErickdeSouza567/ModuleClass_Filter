import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Usando um caminho relativo
df = pd.read_csv("iris.csv")

# Exibindo as primeiras linhas do DataFrame
#print(df.head())

#print(df.shape)

#print(df.info())

#print(df.describe())

#print(df.isnull().sum())

#data = df.drop_duplicates(subset ="species")

print(df.value_counts("species"))

sns.countplot(x='species', data=df)
plt.show()

sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

sns.pairplot(df, hue='species', height=2)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Gráfico 1: Sepal Length
axes[0, 0].set_title("Sepal Length")
axes[0, 0].hist(df['sepal_length'], bins=7)

# Gráfico 2: Sepal Width
axes[0, 1].set_title("Sepal Width")
axes[0, 1].hist(df['sepal_width'], bins=5)

# Gráfico 3: Petal Length
axes[1, 0].set_title("Petal Length")
axes[1, 0].hist(df['petal_length'], bins=6)

# Gráfico 4: Petal Width
axes[1, 1].set_title("Petal Width")
axes[1, 1].hist(df['petal_width'], bins=6)

plt.tight_layout()  # Ajusta o layout para não sobrepor elementos
plt.show()


plot = sns.FacetGrid(df, hue="species")
plot.map(sns.distplot, "sepal_length").add_legend()

plot = sns.FacetGrid(df, hue="species")
plot.map(sns.distplot, "sepal_width").add_legend()

plot = sns.FacetGrid(df, hue="species")
plot.map(sns.distplot, "petal_length").add_legend()

plot = sns.FacetGrid(df, hue="species")
plot.map(sns.distplot, "petal_width").add_legend()

plt.show()

