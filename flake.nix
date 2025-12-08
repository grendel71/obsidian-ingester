{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
  };
  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          nodejs_20
          nodePackages.typescript
          #ta-lib
          (python3.withPackages(ps: with ps; [
		sysrsync
		jupyter
		pandas
		pytesseract
		pdf2image
		google-genai
		ollama
		pillow
		requests
		python-magic
		transformers
		streamlit
		tqdm	
		opencv-python
		numpy
		pymupdf
          ]))
        ];
        #shellHook = "jupyter notebook";
      };
    }
  );
}
