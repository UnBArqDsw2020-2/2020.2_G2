import React from "react";
import Feed from "./components/Feed";
import Header from "./components/Header/Header";
import MudeSeuEstilo from "./components/MudeSeuEstilo/MudeSeuEstilo";
import DescubraUmNovoEstilo from "./components/DescubraUmNovoEstilo/DescubraUmNovoEstilo";
import Button from "@material-ui/core/Button";
import "./Home.css";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  root: {
    fontWeight: "bold",
    color: "black",
    borderColor: " white",
    backgroundColor: "#FFB037",
  },
});

function Home() {
  const classes = useStyles();
  return (
    <>
      <Header>
        <div className="content">
          <div className="options">
            <a href="#">Todos</a>
            <a href="#">Barba</a>
            <a href="#">Cabelo</a>
            <a href="#">Unha</a>
            <a href="#">Estética</a>
          </div>
          <div>
            <Button
              variant="filled"
              classes={{ root: classes.root }}
              size="large"
            >
              Cadastre-se
            </Button>
          </div>
        </div>
      </Header>
      <MudeSeuEstilo />
      <DescubraUmNovoEstilo />
      <Feed />
    </>
  );
}

export default Home;
