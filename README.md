# Regression Metrics Python
 Statistical estimators used in regression or optimization problems.
 Implemented metrics:
 * **RSS** (Residual Sum of Squares):
 $$\text{RSS}=\sum_{ i=1 }^{ l }{ { \left( { \hat { y }  }_{ i }-{ y }_{ i }\right )  }^{ 2 } }$$
 * **MSE** (Mean Squared Error):
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
