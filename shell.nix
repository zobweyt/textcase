let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    uv
    just
    git-cliff
  ];

  shellHook = ''
    just init > /dev/null 2>&1

    if command -v zsh > /dev/null; then
      exec zsh
    fi
  '';
}
