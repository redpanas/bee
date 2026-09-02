{ lib, stdenvNoCC, makeWrapper, curl, gnused }:

stdenvNoCC.mkDerivation {
  pname = "bee";
  version = "1.0.0";
  src = ../..;

  nativeBuildInputs = [ makeWrapper ];

  installPhase = ''
    runHook preInstall
    install -Dm755 bee $out/bin/bee
    wrapProgram $out/bin/bee \
      --prefix PATH : ${lib.makeBinPath [ curl gnused ]}
    runHook postInstall
  '';

  meta = {
    description = "The holy scripture downloader";
    homepage = "https://github.com/redpanas/bee";
    license = lib.licenses.mit;
    mainProgram = "bee";
    platforms = lib.platforms.unix;
  };
}
