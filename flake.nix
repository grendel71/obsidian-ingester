{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-25.11";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python3.withPackages(ps: with ps; [
		sysrsync
		pandas
		requests
          ]))
        ];
      };
    }
  );
}
