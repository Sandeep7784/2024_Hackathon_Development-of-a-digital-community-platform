import React, { useState } from "react";
import Header from "./Header";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import Paper from "@mui/material/Paper";
import List from "@mui/material/List";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Checkbox from "@mui/material/Checkbox";
import Typography from "@mui/material/Typography";

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

const TransferList = ({
  leftList = [],
  rightList = [],
  setRightList,
  handleCreateRequest,
}) => {
  const [checked, setChecked] = useState([]);
  const [left, setLeft] = useState([0, 1, 2, 3]);
  const [right, setRight] = useState([4, 5, 6, 7]);

  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const handleAllRight = () => {
    setRight(right.concat(left));
    setLeft([]);
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setLeft(not(left, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setLeft(left.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };

  const handleAllLeft = () => {
    setLeft(left.concat(right));
    setRight([]);
  };

  return (
    <React.Fragment>
      <Header />
      <Grid container spacing={2} justifyContent="center" alignItems="center">
        <Grid item xs={12}>
          <Typography variant="h5" align="center" gutterBottom>
            Task Transfer List
          </Typography>
        </Grid>
        <Grid item xs={6}>
          <Typography variant="h6">List of Tasks</Typography>
          <Paper sx={{ width: "100%", overflow: "auto" }}>
            <List dense component="div" role="list">
              {left.map((value) => {
                const labelId = `transfer-list-item-${value}-label`;

                return (
                  <ListItemButton
                    key={value}
                    role="listitem"
                    onClick={handleToggle(value)}
                  >
                    <ListItemIcon>
                      <Checkbox
                        checked={checked.indexOf(value) !== -1}
                        tabIndex={-1}
                        disableRipple
                        inputProps={{
                          "aria-labelledby": labelId,
                        }}
                      />
                    </ListItemIcon>
                    <ListItemText
                      id={labelId}
                      primary={`Task ${value + 1}`}
                      secondary={`Description for Task ${value + 1}`}
                    />
                  </ListItemButton>
                );
              })}
            </List>
          </Paper>
        </Grid>
        <Grid item xs={1}>
          <Grid container direction="column" alignItems="center">
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleAllRight}
              disabled={left.length === 0}
              aria-label="move all right"
              title="Move All Right"
            >
              ≫
            </Button>
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleCheckedRight}
              disabled={leftChecked.length === 0}
              aria-label="move selected right"
              title="Move Selected Right"
            >
              &gt;
            </Button>
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleCheckedLeft}
              disabled={rightChecked.length === 0}
              aria-label="move selected left"
              title="Move Selected Left"
            >
              &lt;
            </Button>
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleAllLeft}
              disabled={right.length === 0}
              aria-label="move all left"
              title="Move All Left"
            >
              ≪
            </Button>
          </Grid>
        </Grid>
        <Grid item xs={5}>
          <Typography variant="h6">Selected Tasks</Typography>
          <Paper sx={{ width: "100%", overflow: "auto" }}>
            <List dense component="div" role="list">
              {right.map((value) => {
                const labelId = `transfer-list-item-${value}-label`;

                return (
                  <ListItemButton
                    key={value}
                    role="listitem"
                    onClick={handleToggle(value)}
                  >
                    <ListItemIcon>
                      <Checkbox
                        checked={checked.indexOf(value) !== -1}
                        tabIndex={-1}
                        disableRipple
                        inputProps={{
                          "aria-labelledby": labelId,
                        }}
                      />
                    </ListItemIcon>
                    <ListItemText
                      id={labelId}
                      primary={`Task ${value + 1}`}
                      secondary={`Description for Task ${value + 1}`}
                    />
                  </ListItemButton>
                );
              })}
            </List>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleCreateRequest}
          >
            Add Quest
          </Button>
        </Grid>
      </Grid>
    </React.Fragment>
  );
};

export default TransferList;
