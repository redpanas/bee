class BeeHolyScripture < Formula
  desc "The holy scripture downloader"
  homepage "https://github.com/redpanas/bee"
  url "https://github.com/redpanas/bee.git", tag: "v1.0.0"
  license "MIT"

  depends_on "gnu-sed"

  def install
    bin.install "bee"
  end

  test do
    assert_match "bee 1.0.0", shell_output("#{bin}/bee --version")
  end
end
