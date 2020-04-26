{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>PClass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Allen, Miss Elisabeth Walton</td>\n",
       "      <td>1st</td>\n",
       "      <td>29.00</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Allison, Miss Helen Loraine</td>\n",
       "      <td>1st</td>\n",
       "      <td>2.00</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Allison, Mr Hudson Joshua Creighton</td>\n",
       "      <td>1st</td>\n",
       "      <td>30.00</td>\n",
       "      <td>male</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>\n",
       "      <td>1st</td>\n",
       "      <td>25.00</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allison, Master Hudson Trevor</td>\n",
       "      <td>1st</td>\n",
       "      <td>0.92</td>\n",
       "      <td>male</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                            Name PClass    Age     Sex  \\\n",
       "0                   Allen, Miss Elisabeth Walton    1st  29.00  female   \n",
       "1                    Allison, Miss Helen Loraine    1st   2.00  female   \n",
       "2            Allison, Mr Hudson Joshua Creighton    1st  30.00    male   \n",
       "3  Allison, Mrs Hudson JC (Bessie Waldo Daniels)    1st  25.00  female   \n",
       "4                  Allison, Master Hudson Trevor    1st   0.92    male   \n",
       "\n",
       "   Survived  \n",
       "0         1  \n",
       "1         0  \n",
       "2         0  \n",
       "3         0  \n",
       "4         1  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"titanic.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PClass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1st</td>\n",
       "      <td>29.00</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1st</td>\n",
       "      <td>2.00</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1st</td>\n",
       "      <td>30.00</td>\n",
       "      <td>male</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1st</td>\n",
       "      <td>25.00</td>\n",
       "      <td>female</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1st</td>\n",
       "      <td>0.92</td>\n",
       "      <td>male</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  PClass    Age     Sex  Survived\n",
       "0    1st  29.00  female         1\n",
       "1    1st   2.00  female         0\n",
       "2    1st  30.00    male         0\n",
       "3    1st  25.00  female         0\n",
       "4    1st   0.92    male         1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(['Name'],axis='columns',inplace=True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "inputs = df.drop('Survived',axis='columns')\n",
    "target = df.Survived"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   female  male\n",
       "0       1     0\n",
       "1       1     0\n",
       "2       0     1\n",
       "3       1     0\n",
       "4       0     1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dummies = pd.get_dummies(inputs.Sex)\n",
    "dummies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1st</th>\n",
       "      <th>2nd</th>\n",
       "      <th>3rd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   1st  2nd  3rd\n",
       "0    1    0    0\n",
       "1    1    0    0\n",
       "2    1    0    0\n",
       "3    1    0    0\n",
       "4    1    0    0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dumy = pd.get_dummies(inputs.PClass)\n",
    "dumy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PClass</th>\n",
       "      <th>Age</th>\n",
       "      <th>Sex</th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "      <th>1st</th>\n",
       "      <th>2nd</th>\n",
       "      <th>3rd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1st</td>\n",
       "      <td>29.00</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1st</td>\n",
       "      <td>2.00</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1st</td>\n",
       "      <td>30.00</td>\n",
       "      <td>male</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1st</td>\n",
       "      <td>25.00</td>\n",
       "      <td>female</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1st</td>\n",
       "      <td>0.92</td>\n",
       "      <td>male</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  PClass    Age     Sex  female  male  1st  2nd  3rd\n",
       "0    1st  29.00  female       1     0    1    0    0\n",
       "1    1st   2.00  female       1     0    1    0    0\n",
       "2    1st  30.00    male       0     1    1    0    0\n",
       "3    1st  25.00  female       1     0    1    0    0\n",
       "4    1st   0.92    male       0     1    1    0    0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputs = pd.concat([inputs,dummies],axis='columns')\n",
    "inputs = pd.concat([inputs,dumy],axis='columns')\n",
    "inputs.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "      <th>1st</th>\n",
       "      <th>2nd</th>\n",
       "      <th>3rd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>30.00</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.92</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Age  female  male  1st  2nd  3rd\n",
       "0  29.00       1     0    1    0    0\n",
       "1   2.00       1     0    1    0    0\n",
       "2  30.00       0     1    1    0    0\n",
       "3  25.00       1     0    1    0    0\n",
       "4   0.92       0     1    1    0    0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputs.drop(['Sex','PClass'],axis='columns',inplace=True)\n",
    "inputs.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age'], dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputs.columns[inputs.isna().any()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>female</th>\n",
       "      <th>male</th>\n",
       "      <th>1st</th>\n",
       "      <th>2nd</th>\n",
       "      <th>3rd</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>29.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>30.00</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>25.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.92</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Age  female  male  1st  2nd  3rd\n",
       "0  29.00       1     0    1    0    0\n",
       "1   2.00       1     0    1    0    0\n",
       "2  30.00       0     1    1    0    0\n",
       "3  25.00       1     0    1    0    0\n",
       "4   0.92       0     1    1    0    0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputs.Age = inputs.Age.fillna(inputs.Age.mean())\n",
    "inputs.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1050"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "263"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.naive_bayes import GaussianNB\n",
    "model = GaussianNB()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GaussianNB(priors=None, var_smoothing=1e-09)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7224334600760456"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0 1 0 0 1 1 0 0 0 1\n",
      " 0 0 0 1 0 0 0 0 1 1 0 0 1 0 1 0 0 1 0 0 1 0 1 0 0 0 0 0 1 1 0 0 1 1 1 0 0\n",
      " 1 0 0 1 1 1 1 1 1 1 1 0 0 1 0 0 1 0 1 1 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 1 1\n",
      " 1 0 1 0 0 0 0 1 0 1 0 1 1 0 1 1 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0\n",
      " 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0 1 0 0 0 1 0 0 0 1 0\n",
      " 1 0 0 1 0 0 0 1 0 0 0 0 1 1 0 1 1 0 0 1 0 0 0 0 0 1 0 1 0 0 1 0 0 1 0 0 0\n",
      " 1 1 1 1 0 0 1 0 0 1 0 1 0 1 0 1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 1 1 1 0 0\n",
      " 1 1 1 0]\n"
     ]
    }
   ],
   "source": [
    "print (pred[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7224334600760456"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,\n",
       "    decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',\n",
       "    max_iter=-1, probability=False, random_state=None, shrinking=True,\n",
       "    tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = SVC()\n",
    "model.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6844106463878327"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7452471482889734"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.svm import SVC\n",
    "model = SVC(C=50.0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7452471482889734"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.svm import SVC\n",
    "model = SVC(C=500.0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7870722433460076"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import tree\n",
    "model = tree.DecisionTreeClassifier()\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7870722433460076"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier()\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7870722433460076"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=5)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7452471482889734"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.svm import SVC\n",
    "model = SVC(C=500.0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7718631178707225"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=50)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7908745247148289"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=10)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7756653992395437"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=19)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=6)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.779467680608365"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=7)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7946768060836502"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=8)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=9)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7680608365019012"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=11)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7832699619771863"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=12)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7946768060836502"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=13)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7870722433460076"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=14)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7946768060836502"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=15)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.779467680608365"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=16)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "model = KNeighborsClassifier(n_neighbors=9)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=100, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8098859315589354"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=10, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7452471482889734"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=1, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=50, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8174904942965779"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=5, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8174904942965779"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=5, random_state=1)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8022813688212928"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=100, random_state=5)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7490494296577946"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=4, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8288973384030418"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=3, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7452471482889734"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=2, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7984790874524715"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=35, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8098859315589354"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=18, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8288973384030418"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "model = AdaBoostClassifier(n_estimators=3, random_state=0)\n",
    "model.fit(X_train,y_train)\n",
    "pred = model.predict(X_test)\n",
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test, pred)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
