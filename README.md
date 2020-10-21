# Regression Metrics Python
 Statistical estimators used in regression or optimization problems.
 Implemented metrics:
 * **RSS** (Residual Sum of Squares):
 ![\large RSS=\sum_{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i }\right )  }^{ 2 } }] (https://latex.codecogs.com/svg.latex?\large&space;RSS=\sum_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}\right&space;)&space;}^{&space;2&space;}&space;})
 
 \(\text{RSS}=\sum_{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i }\right )  }^{ 2 } }\)
 
 * **MSE** (Mean Squared Error):
 ![MSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i } \right)  }^{ 2 } }  }{ l }](<img src="https://latex.codecogs.com/svg.latex?\large&space;MSE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;\right)&space;}^{&space;2&space;}&space;}&space;}{&space;l&space;}" title="\large MSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y } }_{ i }-{ y }_{ i } \right) }^{ 2 } } }{ l }" />)
 $$MSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i } \right)  }^{ 2 } }  }{ l } $$
 
 
 * **MSPE** (Mean Squared Percentage Error):
 $$MSEP=\frac { \sum _{ i=1 }^{ l }{ { \left( \frac { { \hat { y }  }_{ i }-{ y }_{ i } }{ { y }_{ i } }  \right)  }^{ 2 } }  }{ l } \times 100$$
 * **RMSE** (Root-Mean-Square Error):
 $$RMSE=\sqrt { MSE } $$
 * **RMSPE** (Root-Mean-Square Percentage Error):
 $$RMSEP=\sqrt { MSEP } \times 100$$
 * **MAE** (Mean Absolute Error):
 $$MAE=\frac { \sum _{ i=1 }^{ l }{ \left| { \hat { y }  }_{ i }-{ y }_{ i } \right|  }  }{ l } $$
 * **MAPE** (Mean Absolute Percentage Error):
 $$MAPE=\frac { \sum _{ i=1 }^{ l }{ \left| \frac { { \hat { y }  }_{ i }-{ y }_{ i } }{ { y }_{ i } }  \right|  }  }{ l } \times 100$$
 * **RSE** (Relative Squared Error):
 $$RSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i } \right)  }^{ 2 } }  }{ \sum _{ i=1 }^{ l }{ { \left( { \overline { y }  }-{ y }_{ i } \right)  }^{ 2 } }  } $$
 * **RAE** (Relative Absolute Error):
 $$RAE=\frac { \sum _{ i=1 }^{ l }{ \left| { \hat { y }  }_{ i }-{ y }_{ i } \right|  }  }{ \sum _{ i=1 }^{ l }{ \left| \overline { y } -{ y }_{ i } \right|  }  } $$
 * **R2** (Coefficient of determination):
 $$R2=1-RSE$$
Where ${y}_{i}$ is the actual value, ${ \hat { y }  }_{ i }$ is the forecasted value, $\overline { y }$ and $l$ are the average of the $y$ variable and the number of samples, respectively.
