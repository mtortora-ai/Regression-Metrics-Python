# Regression Metrics Python
 Statistical estimators used in regression or optimization problems.
 Implemented metrics:
 * **RSS** (Residual Sum of Squares):
 
<p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;RSS=\sum_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;ii&space;}-{&space;y&space;}_{&space;i&space;}\right&space;)&space;}^{&space;2&space;}&space;}" title="\large RSS=\sum_{ i=1 }^{ l }{ { \left( { \hat { y } }_{ ii }-{ y }_{ i }\right ) }^{ 2 } }" /> 
</p>
 
 * **MSE** (Mean Squared Error):
 
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;MSE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;\right)&space;}^{&space;2&space;}&space;}&space;}{&space;l&space;}" title="\large MSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y } }_{ i }-{ y }_{ i } \right) }^{ 2 } } }{ l }" />
  </p>

 
 * **MSPE** (Mean Squared Percentage Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;MSPE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;\frac&space;{&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;}{&space;{&space;y&space;}_{&space;i&space;}&space;}&space;\right)&space;}^{&space;2&space;}&space;}&space;}{&space;l&space;}&space;\times" title="\large MSPE=\frac { \sum _{ i=1 }^{ l }{ { \left( \frac { { \hat { y } }_{ i }-{ y }_{ i } }{ { y }_{ i } } \right) }^{ 2 } } }{ l } \times" />
 </p>
 
 * **RMSE** (Root-Mean-Square Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;RMSE=\sqrt&space;{&space;MSE&space;}" title="\large RMSE=\sqrt { MSE }" />
 </p>
 * **RMSPE** (Root-Mean-Square Percentage Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;RMSEP=\sqrt&space;{&space;MSEP&space;}&space;\times&space;100" title="\large RMSEP=\sqrt { MSEP } \times 100" />
 </p>
 * **MAE** (Mean Absolute Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;MAE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;\left|&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;\right|&space;}&space;}{&space;l&space;}" title="\large MAE=\frac { \sum _{ i=1 }^{ l }{ \left| { \hat { y } }_{ i }-{ y }_{ i } \right| } }{ l }" />
 </p>
 * **MAPE** (Mean Absolute Percentage Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;MAPE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;\left|&space;\frac&space;{&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;}{&space;{&space;y&space;}_{&space;i&space;}&space;}&space;\right|&space;}&space;}{&space;l&space;}&space;\times&space;100" title="\large MAPE=\frac { \sum _{ i=1 }^{ l }{ \left| \frac { { \hat { y } }_{ i }-{ y }_{ i } }{ { y }_{ i } } \right| } }{ l } \times 100" />
 </p>
 * **RSE** (Relative Squared Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;RSE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;\right)&space;}^{&space;2&space;}&space;}&space;}{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;{&space;\left(&space;{&space;\overline&space;{&space;y&space;}&space;}-{&space;y&space;}_{&space;i&space;}&space;\right)&space;}^{&space;2&space;}&space;}&space;}" title="\large RSE=\frac { \sum _{ i=1 }^{ l }{ { \left( { \hat { y } }_{ i }-{ y }_{ i } \right) }^{ 2 } } }{ \sum _{ i=1 }^{ l }{ { \left( { \overline { y } }-{ y }_{ i } \right) }^{ 2 } } }" />
 </p>

 * **RAE** (Relative Absolute Error):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;RAE=\frac&space;{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;\left|&space;{&space;\hat&space;{&space;y&space;}&space;}_{&space;i&space;}-{&space;y&space;}_{&space;i&space;}&space;\right|&space;}&space;}{&space;\sum&space;_{&space;i=1&space;}^{&space;l&space;}{&space;\left|&space;\overline&space;{&space;y&space;}&space;-{&space;y&space;}_{&space;i&space;}&space;\right|&space;}&space;}" title="\large RAE=\frac { \sum _{ i=1 }^{ l }{ \left| { \hat { y } }_{ i }-{ y }_{ i } \right| } }{ \sum _{ i=1 }^{ l }{ \left| \overline { y } -{ y }_{ i } \right| } }" />
 </p>
 
 * **R2** (Coefficient of determination):
 <p align="center">
 <img src="https://latex.codecogs.com/svg.latex?\large&space;R2=1-RSE" title="\large R2=1-RSE" />
 </p>

Where ${y}_{i}$ is the actual value, ${ \hat { y }  }_{ i }$ is the forecasted value, $\overline { y }$ and $l$ are the average of the $y$ variable and the number of samples, respectively.
